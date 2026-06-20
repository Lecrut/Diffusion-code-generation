TRUE = 'true'
FALSE = 'false'

def validate_and_count(input_data):
    try:
        values = input_data.split(',')
        true_count = sum(1 for value in values if value.strip().lower() == TRUE)
        false_count = sum(1 for value in values if value.strip().lower() == FALSE)
        return true_count, false_count
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

if __name__ == '__main__':
    input_data = "true,false,true,true,false"
    try:
        true_count, false_count = validate_and_count(input_data)
        print(f"True count: {true_count}")
        print(f"False count: {false_count}")
    except ValueError as e:
        print(e)