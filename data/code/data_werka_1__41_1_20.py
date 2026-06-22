def manipulate_case(input_string):
    return {
        'lowercase': input_string.lower(),
        'uppercase': input_string.upper(),
        'titlecase': input_string.title()
    }

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = manipulate_case(sample_input)
    print(result)