import sys
def process_text(input_text):
    return input_text.lower()
if __name__ == '__main__':
    sample_input = "HeLlO WoRlD"
    output_text = process_text(sample_input)
    print(output_text)