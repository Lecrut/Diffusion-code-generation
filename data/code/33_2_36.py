def remove_spaces(input_string):
    return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_text = "Competitive programming requires quick thinking."
    processed_text = remove_spaces(sample_text)
    print(processed_text)