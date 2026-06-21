def extract_names(pipeline_string):
    return pipeline_string.split('|')

if __name__ == '__main__':
    sample_input = "Alice|Bob|Charlie"
    print(extract_names(sample_input))