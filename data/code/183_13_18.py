def pipe_to_list(names):
    return [name.strip() for name in names.split('|') if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David|Eve"
    cleaned_names = pipe_to_list(sample_names)
    print(cleaned_names)