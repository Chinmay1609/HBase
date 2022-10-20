import happybase

connection = happybase.Connection('quickstart.cloudera
')
table = connection.table('customer')

table.put(b'Chinmay', {b'family:address': b'City',
                       b'family:Order': b'id'})

row = table.row(b'Chinmay')
print(row[b'family:address',b'family:Order'])  # prints 'value1','value2'

for key, data in table.rows([b'Chinmay']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'Chinmay'):
    print(key, data)  # prints 'value1' and 'value2'


