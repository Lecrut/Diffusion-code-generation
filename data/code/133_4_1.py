if __name__ == '__main__':
    sample_input = "true,false,true,true,false"
    try:
        values = sample_input.split(',')
        true_count = 0
        false_count = 0
        for value in values:
            if value.strip().lower() == 'true':
                true_count += 1
            elif value.strip().lower() == 'false':
                false_count += 1
            else:
                print(f"Error: Invalid value encountered: {value}")
                exit(1)
        print(f"True count: {true_count}")
        print(f"False count: {false_count}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")