from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

class Command(BaseCommand):

    def handle(self,*args,**options):
        self.stdout.write('waiting for database...')
        db_up = False
        '''
        Keep checking until the database is ready
        We are sleeping for 1 second, cz we dont want to continously
        hit the database method
        '''
        while db_up is False: 
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting for 1 second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!!'))        