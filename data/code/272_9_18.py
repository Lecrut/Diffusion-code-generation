import csv

def read_words_from_csv(file_path):
    with open(file_path, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        words = list(reader)
    return words

def sort_words_by_first_column(words):
    return sorted(words, key=lambda row: row[0])

def write_words_to_csv(file_path, words):
    with open(file_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(words)

if __name__ == '__main__':
    input_file = 'input.csv'
    output_file = 'output.csv'
    
    words = read_words_from_csv(input_file)
    sorted_words = sort_words_by_first_column(words)
    write_words_to_csv(output_file, sorted_words)