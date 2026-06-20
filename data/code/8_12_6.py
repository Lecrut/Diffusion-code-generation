import csv
import io

def split_by_commas_preserving_quotes(input_string):
    if not input_string:
        return []
    reader = csv.reader(io.StringIO(input_string), quoting=csv.QUOTE_ALL)
    for row in reader:
        return [token.strip() for token in row]
    return []

if __name__ == '__main__':
    sample = '"Hello, World", foo, "bar, baz", qux'
    result = split_by_commas_preserving_quotes(sample)
    print(result)