import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv(dotenv_path="./.env")

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected to Neo4j' AS message")
        for record in result:
            print(record["message"])

test_connection()
driver.close()