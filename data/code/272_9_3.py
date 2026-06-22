import csv

def sort_words_by_first_column(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        words = list(reader)
    
    words.sort(key=lambda row: row[0])
    
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(words)

if __name__ == '__main__':
    sort_words_by_first_column('input.csv', 'output.csv')