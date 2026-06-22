import csv
import io

def split_by_comma_preserve_quotes(input_string):
    reader = csv.reader(io.StringIO(input_string))
    for row in reader:
        return row
    return []

if __name__ == '__main__':
    test_input = 'apple,"banana, berry",cherry,"date, elderberry"'
    result = split_by_comma_preserve_quotes(test_input)
    print(result)