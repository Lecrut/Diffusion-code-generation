def count_character_types(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    uppercase_count = sum(1 for char in content if char.isupper())
    lowercase_count = sum(1 for char in content if char.islower())
    digit_count = sum(1 for char in content if char.isdigit())
    special_count = sum(1 for char in content if not char.isalnum())
    
    with open(output_file, 'w') as file:
        file.write(f"Uppercase: {uppercase_count}\n")
        file.write(f"Lowercase: {lowercase_count}\n")
        file.write(f"Digits: {digit_count}\n")
        file.write(f"Special Characters: {special_count}\n")

if __name__ == '__main__':
    count_character_types('sample.txt', 'output.txt')