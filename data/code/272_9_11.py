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
    input_sample = 'sample_input.csv'
    output_sample = 'sample_output.csv'
    with open(input_sample, mode='w', newline='') as infile:
        writer = csv.writer(infile)
        writer.writerow(['cherry', 'apple'])
        writer.writerow(['banana', 'date'])
        writer.writerow(['elderberry', 'fig'])
    sort_words_by_first_column(input_sample, output_sample)
    with open(output_sample, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        sorted_words = list(reader)
        print(sorted_words)