def concatenate_strings(first_part, second_part):
    combined_result = first_part + second_part
    return combined_result

if __name__ == '__main__':
    prefix = "Good morning, "
    suffix = "Earth!"
    greeting = concatenate_strings(prefix, suffix)
    print(greeting)