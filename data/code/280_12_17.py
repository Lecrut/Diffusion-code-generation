def repeat_task(task, times):
    for _ in range(times):
        task()

if __name__ == '__main__':
    def my_task():
        print("Task executed")

    repeat_task(my_task, 10)