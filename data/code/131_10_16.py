class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

def gini_index(groups):
    total = sum(len(group) for group in groups)
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in set([row[-1] for row in group]):
            p = [row[-1] for row in group].count(class_val) / size
            score += p * (1.0 - p)
        gini += (size / total) * score
    return gini

def split(dataset, feature, threshold):
    left, right = [], []
    for row in dataset:
        if row[feature] < threshold:
            left.append(row)
        else:
            right.append(row)
    return left, right

def get_best_split(dataset):
    best_index, best_value, best_score, best_groups = None, None, float('inf'), None
    for i in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = split(dataset, i, row[i])
            gini = gini_index(groups)
            if gini < best_score:
                best_index, best_value, best_score, best_groups = i, row[i], gini, groups
    return {'index': best_index, 'value': best_value, 'groups': best_groups}

def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

def build_tree(train, max_depth=0, min_size=1):
    root = get_best_split(train)
    if not root['groups']:
        return
    left, right = root['groups']
    if len(left) <= min_size:
        root['left'] = to_terminal(left)
    elif max_depth == 0:
        root['left'] = build_tree(left, 1, min_size)
    else:
        root['left'] = build_tree(left, max_depth - 1, min_size)
    if len(right) <= min_size:
        root['right'] = to_terminal(right)
    elif max_depth == 0:
        root['right'] = build_tree(right, 1, min_size)
    else:
        root['right'] = build_tree(right, max_depth - 1, min_size)
    return root

def predict(node, row):
    if row[node['feature']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

def decision_tree_classifier(train, test, max_depth=0, min_size=1):
    tree = build_tree(train, max_depth, min_size)
    predictions = [predict(tree, row) for row in test]
    return predictions

if __name__ == '__main__':
    dataset = [
        [2.771244718, 1.784783929, 0],
        [1.728571336, 1.169761413, 0],
        [3.678319846, 2.81281357, 0],
        [3.961043357, 2.61995032, 0],
        [2.999208922, 2.209014212, 0],
        [7.497545867, 3.162953546, 1],
        [9.00220326, 3.339047188, 1],
        [7.444542326, 0.476683375, 1],
        [10.12493903, 3.234550982, 1],
        [6.642287351, 3.319983761, 1],
        [8.82736367, 3.627555369, 1],
        [4.782750426, 3.64954983, 0],
        [5.42421445, 3.105305496, 0],
        [4.696522875, 1.858733033, 0],
        [7.229671956, 2.669141628, 0],
        [8.121679154, 3.16717137, 1],
        [5.332441249, 2.088626776, 0],
        [6.922596716, 1.77106367, 0],
        [8.675418651, -0.242068655, 1]
    ]
    train = dataset[:10]
    test = dataset[10:]
    predictions = decision_tree_classifier(train, test)
    print(predictions)