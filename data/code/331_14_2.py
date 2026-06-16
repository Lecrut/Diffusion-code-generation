import sys
def modify_to_lowercase(text):
    return text.lower()
if __name__ == '__main__':
    sample_input = "This Is A Sample String For Lowercasing"
    modified_output = modify_to_lowercase(sample_input)
    print(modified_output)