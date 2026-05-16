if __name__ == '__main__':
    input_data = "true,false,true,true,false,true"
    try:
        values = input_data.split(',')
        true_count = 0
        false_count = 0
        for value in values:
            if value.strip() == "true":
                true_count += 1
            elif value.strip() == "false":
                false_count += 1
            else:
                print(f"Error: Invalid value encountered: '{value}'")
                exit(1)
        print(f"True count: {true_count}")
        print(f"False count: {false_count}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")