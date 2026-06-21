import csv

def extract_first_column(csv_string):
    first_column_values = []
    reader = csv.reader(csv_string.splitlines(), quotechar='"')
    for row in reader:
        if row:
            first_column_values.append(row[0])
    return first_column_values
if __name__ == '__main__':
    sample_csv1 = '"apple","red","fruit"\n"banana","yellow","fruit"'
    sample_csv2 = '"carrot","orange","vegetable"'
    print(extract_first_column(sample_csv1))
    print(extract_first_column(sample_csv2))