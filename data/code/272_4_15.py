def sort_words_from_file(input_path, output_path):
    try:
        with open(input_path, 'r') as file:
            words = file.read().split()
        sorted_words = sorted(words)
        with open(output_path, 'w') as file:
            for word in sorted_words:
                file.write(word + '\n')
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    sort_words_from_file('sample_input.txt', 'sorted_output.txt')