import matplotlib.pyplot as plt
def AND(a, b):
    return a & b
def OR(a, b):
    return a | b
def NOT(a):
    return 1 - a
if __name__ == '__main__':
    print("--- AND Gate Demonstration ---")
    a_and = 0
    b_and = 0
    print(f"AND(0, 0) = {AND(a_and, b_and)}")
    a_and = 0
    b_and = 1
    print(f"AND(0, 1) = {AND(a_and, b_and)}")
    a_and = 1
    b_and = 0
    print(f"AND(1, 0) = {AND(a_and, b_and)}")
    a_and = 1
    b_and = 1
    print(f"AND(1, 1) = {AND(a_and, b_and)}")
    print("\n--- OR Gate Demonstration ---")
    a_or = 0
    b_or = 0
    print(f"OR(0, 0) = {OR(a_or, b_or)}")
    a_or = 0
    b_or = 1
    print(f"OR(0, 1) = {OR(a_or, b_or)}")
    a_or = 1
    b_or = 0
    print(f"OR(1, 0) = {OR(a_or, b_or)}")
    a_or = 1
    b_or = 1
    print(f"OR(1, 1) = {OR(a_or, b_or)}")
    print("\n--- NOT Gate Demonstration ---")
    a_not = 0
    print(f"NOT(0) = {NOT(a_not)}")
    a_not = 1
    print(f"NOT(1) = {NOT(a_not)}")
    print("\n--- Visual Demonstration (AND, OR, NOT) ---")
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    results_and = [AND(a, b) for a, b in inputs]
    results_or = [OR(a, b) for a, b in inputs]
    results_not = [NOT(a) for a in [0, 1]]
    fig, axes = plt.subplots(1, 3, figsize=(10, 4))
    axes[0].set_title("AND Gate")
    axes[0].set_xticks([0, 1])
    axes[0].set_yticks([0, 1])
    axes[0].grid(True)
    axes[0].set_visible(False)
    axes[1].set_title("OR Gate")
    axes[1].set_xticks([0, 1])
    axes[1].set_yticks([0, 1])
    axes[1].grid(True)
    axes[1].set_visible(False)
    axes[2].set_title("NOT Gate")
    axes[2].set_xticks([0, 1])
    axes[2].set_yticks([0, 1])
    axes[2].grid(True)
    axes[2].set_visible(False)