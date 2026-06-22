def repeat_action():
    action = lambda: print("Action repeated")
    try:
        for _ in range(3):
            action()
    except Exception as e:
        print(f"Error during repetition: {e}")

if __name__ == '__main__':
    repeat_action()