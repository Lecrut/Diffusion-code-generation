MAX_ITERATIONS = 10

def repeat_action():
    return "Action repeated"

if __name__ == '__main__':
    results = [repeat_action() for _ in range(MAX_ITERATIONS)]
    print(results)