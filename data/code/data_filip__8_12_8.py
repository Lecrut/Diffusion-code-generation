import csv
import io

def split_comma_preserve_quotes(input_string):
    reader = csv.reader(io.StringIO(input_string))
    for row in reader:
        return row
    return []

if __name__ == '__main__':
    sample = 'apple,"banana, cherry",date,"fig, grape"'
    result = split_comma_preserve_quotes(sample)
    print(result)