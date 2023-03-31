import sqlite3

def create_connection():
    # Create a database connection
    conn = sqlite3.connect('example.db')
    return conn

def create_tables(conn):
    # Create a cursor object
    c = conn.cursor()

    # Create clients table
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (Name text, Notes text)''')

    # Create products table
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (Name text, Price real, Notes text)''')

    # Create sell table
    c.execute('''CREATE TABLE IF NOT EXISTS sell
                 (Name text, product_purchase text, usd_sell real, cup_sell real, usd_pay real, cup_pay real)''')

    # Save (commit) the changes
    conn.commit()

def add_client(conn, name, notes):
    # Create a cursor object
    c = conn.cursor()
    
    # Insert a new client into the clients table
    c.execute("INSERT INTO clients VALUES (?, ?)", (name, notes))
    
    # Save (commit) the changes
    conn.commit()

def add_product(conn, name, price, notes):
    # Create a cursor object
    c = conn.cursor()
    
    # Insert a new product into the products table
    c.execute("INSERT INTO products VALUES (?, ?, ?)", (name, price, notes))
    
    # Save (commit) the changes
    conn.commit()

def add_sell(conn, name, product_purchase, usd_sell, cup_sell, usd_pay, cup_pay):
    # Create a cursor object
    c = conn.cursor()
    
    # Insert a new sell into the sell table
    c.execute("INSERT INTO sell VALUES (?, ?, ?, ?, ?, ?)", (name, product_purchase, usd_sell, cup_sell, usd_pay, cup_pay))
    
    # Save (commit) the changes
    conn.commit()

# Example usage:
conn = create_connection()  # Create a database connection
create_tables(conn)  # Create tables

# Add data to tables
add_client(conn, 'John Doe', 'Regular customer')
add_product(conn, 'Product A', 9.99, 'Popular item')
add_sell(conn,'John Doe', 'Product A', 9.99 , 0 , 9.99 , 0)

conn.close()  # Close the database connection
