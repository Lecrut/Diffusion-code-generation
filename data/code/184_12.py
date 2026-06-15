import os
def check_for_forbidden_words(filepath, forbidden_words):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            line = line.lower()
            for word in forbidden_words:
                if word in line:
                    print(f"Line {line_number}: Forbidden word found: '{word}'")
if __name__ == '__main__':
    sample_filename = "sample_input.txt"
    forbidden_list = ["bad", "evil", "secret"]
    with open(sample_filename, 'w', encoding='utf-8') as f:
        f.write("This is a good line.\n")
        f.write("We found some bad data here.\n")
        f.write("The secret plan is safe.\n")
        f.write("Another line without issues.\n")
    check_for_forbidden_words(sample_filename, forbidden_list)
    os.remove(sample_filename)