import csv
import io

def split_by_comma_preserving_quotes(input_string):
    reader = csv.reader(io.StringIO(input_string))
    for row in reader:
        return row
    return []

if __name__ == '__main__':
    sample_input = 'apple,"banana, berry",cherry,"date, ""fig""",elderberry'
    result = split_by_comma_preserving_quotes(sample_input)
    print(result)