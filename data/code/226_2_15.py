REPETITIONS = 100
if __name__ == '__main__':
    hello_world_list = ['Hello World' for _ in range(REPETITIONS)]
    result = '\n'.join(hello_world_list)
    print(result)