if __name__ == '__main__':
    condition_a = True
    condition_b = False
    try:
        result = condition_a and condition_b
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(result)