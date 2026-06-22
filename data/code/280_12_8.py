def repeat_task(task, count):
    for _ in range(count):
        task()

if __name__ == '__main__':
    def sample_task():
        print("Task repeated")
    
    repeat_task(sample_task, 10)