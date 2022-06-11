from seleniumbase import BaseCase
import pandas as pd
import snowflake.connector
conn = snowflake.connector.connect(user='INNOKENTYVOLOSHIN', password='1Q2w3e4r', account='iwb20380.us-east-1')


class Tests(BaseCase):

    def test_data(self):
        sql = """
        -- auto-generated definition
        insert into JENKINSTEST.PUBLIC.TEST_EXECUTION_RESULTS (EXECUTION_ID, PROCESS_NAME, CATEGORY, STATUS)
        select 'absce','Usage - Fetch Data from Bob','Integration (BI)','SUCCESS'
        union
        select 'absce','Usage - Import Data into Netsuite','Integration','FAILED';
        """

        query = conn.cursor().execute(sql).fetchall()

        sql2 = """
        SELECT * FROM JENKINSTEST.PUBLIC.TEST_EXECUTION_RESULTS;
        """

        query2 = conn.cursor().execute(sql2).fetchall()

        df = pd.DataFrame(query2)
        print(df)

    def test_backend(self):
        pass

    def test_frontend(self):
        self.open("https://practice.automationbro.com")

        self.assert_title("Practice E-Commerce Site - Automation Bro")
