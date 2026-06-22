import csv

class WordSorter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    
    def read_words(self):
        with open(self.input_file, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            return list(reader)
    
    def sort_words(self, words):
        return sorted(words, key=lambda row: row[0])
    
    def write_words(self, words):
        with open(self.output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(words)

if __name__ == '__main__':
    sorter = WordSorter('input.csv', 'output.csv')
    words = sorter.read_words()
    sorted_words = sorter.sort_words(words)
    sorter.write_words(sorted_words)
    print("Words written to output.csv")