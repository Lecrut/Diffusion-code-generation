import csv
from io import StringIO
def parse_csv_data(csv_string):
    f = StringIO(csv_string)
    reader = csv.DictReader(f)
    return list(reader)
if __name__ == '__main__':
    sample_csv = "header1,header2,header3\nvalue1a,value1b,value1c\nvalue2a,value2b,value2c"
    result = parse_csv_data(sample_csv)
    print(result)