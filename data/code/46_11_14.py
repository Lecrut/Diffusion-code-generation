import pandas as pd

def get_max_salary(salary_list):
    df = pd.DataFrame(salary_list, columns=['salary'])
    return df['salary'].max()

if __name__ == '__main__':
    sample_data = [45000, 52000, 67000, 38000, 71000]
    print(get_max_salary(sample_data))