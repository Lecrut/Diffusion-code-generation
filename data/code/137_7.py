if __name__ == '__main__':
    choice = 2
    message = "You selected option 2." if choice == 2 else ("You selected option 1." if choice == 1 else "You selected option 3.")
    print(message)