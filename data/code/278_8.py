import sys
def process_items(input_string):
    items = input_string.split()
    for item in items:
        print(item)
if __name__ == '__main__':
    sample_input = "apple banana cherry date"
    process_items(sample_input)