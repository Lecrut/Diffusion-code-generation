if __name__ == '__main__':
    try:
        rows = 5
        triangle_pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
        print(triangle_pattern)
    except Exception as e:
        print(f"An error occurred: {e}")