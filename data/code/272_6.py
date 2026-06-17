import os
input_filename = "input.txt"
output_filename = "sorted_output.txt"
with open(input_filename, 'w') as f:
    f.write("apple\nbanana\ncherry\ndate\nelephant\nfig")
words = []
try:
    with open(input_filename, 'r') as infile:
        for line in infile:
            words.append(line.strip())
except FileNotFoundError:
    print(f"Error: Input file {input_filename} not found.")
    exit()
sorted_words = sorted(words)
with open(output_filename, 'w') as outfile:
    for word in sorted_words:
        outfile.write(word + '\n')
if __name__ == '__main__':
    pass