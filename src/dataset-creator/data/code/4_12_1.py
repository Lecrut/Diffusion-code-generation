import time
def process_selection(choice: int) -> None:
    if choice == 1:
        print("Option 1 selected: Initializing standard protocol.")
        data = [1, 2, 3]
        result = sum(data) * 2
        time.sleep(0.5)
    elif choice == 2:
        print("Option 2 selected: Activating high-performance mode.")
        large_list = list(range(1_000_000))
        start_time = time.perf_counter()
        filtered = [x for x in large_list if x % 3 == 0]
        end_time = time.perf_counter()
        print(f"Processed {len(filtered)} items. Time taken: {(end_time - start_time):.4f}s")
    elif choice == 3:
        print("Option 3 selected: Running dynamic simulation.")
        values = [10, 20, 30]
        for i in range(5):
            current_val = sum(values) + (i * 10)
            if current_val > 100:
                print(f"Threshold exceeded at iteration {i}")
if __name__ == '__main__':
    choices = [1, 2, 3]
    for selected_choice in choices:
        process_selection(selected_choice)