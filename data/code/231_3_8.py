def repeat_and_flatten():
    try:
        result = [('X', 'Y')] * 5
        flattened_result = [item for sublist in result for item in sublist]
        return flattened_result
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print(repeat_and_flatten())