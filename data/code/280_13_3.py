def perform_task(param):
    return f"Task performed with {param}"

if __name__ == '__main__':
    parameters = ['a', 'b', 'c', 'd', 'e']
    results = [perform_task(p) for p in parameters]
    print(results)