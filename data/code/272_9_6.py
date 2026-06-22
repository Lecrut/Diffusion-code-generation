import csv

def read_words_from_csv(file_path):
    with open(file_path, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        words = list(reader)
    return words

def sort_words_by_first_column(words):
    return sorted(words, key=lambda row: row[0])

def write_sorted_words_to_csv(sorted_words, output_file):
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(sorted_words)

if __name__ == '__main__':
    input_path = 'input.csv'
    output_path = 'output.csv'

    words = read_words_from_csv(input_path)
    sorted_words = sort_words_by_first_column(words)
    write_sorted_words_to_csv(sorted_words, output_path)