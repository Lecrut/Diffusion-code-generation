def repeat_task(task_function, times):
    if not callable(task_function) or not isinstance(times, int) or times < 0:
        raise ValueError("Invalid input: task_function must be callable and times must be a non-negative integer")
    
    counter = 0
    while counter < times:
        task_function()
        counter += 1

if __name__ == '__main__':
    def sample_task():
        print("Task executed")

    number_of_repeats = 10
    repeat_task(sample_task, number_of_repeats)