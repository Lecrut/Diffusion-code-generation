import csv
from io import StringIO

def extract_first_column_values(csv_text):
    if not isinstance(csv_text, str) or not csv_text.strip():
        raise ValueError('Input must be a non-empty string')
    csv_file = StringIO(csv_text)
    reader = csv.reader(csv_file)
    result = [row[0] for row in reader if len(row) > 0]
    return result
if __name__ == '__main__':
    sample_csv1 = 'apple,banana,cherry\n"orange",grape,"lemon"'
    sample_csv2 = '"hello",world,python\n"code",is,"fun"'
    print(extract_first_column_values(sample_csv1))
    print(extract_first_column_values(sample_csv2))