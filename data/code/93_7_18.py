if __name__ == '__main__':
    try:
        a = False
        b = False
        print(not all([a, b]))
    except Exception as e:
        print(f"An error occurred: {e}")