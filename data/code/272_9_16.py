import csv

def sort_words_by_first_column(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        words = list(reader)
    
    sorted_words = sorted(words, key=lambda row: row[0])
    
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(sorted_words)

if __name__ == '__main__':
    input_csv = 'sample_input.csv'
    output_csv = 'sorted_output.csv'
    
    sort_words_by_first_column(input_csv, output_csv)