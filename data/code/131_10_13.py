class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

def gini_impurity(labels):
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return 1 - np.sum(probabilities ** 2)

def split_data(X, y, feature, threshold):
    left_mask = X[:, feature] < threshold
    right_mask = ~left_mask
    return X[left_mask], y[left_mask], X[right_mask], y[right_mask]

def best_split(X, y):
    best_feature = None
    best_threshold = None
    best_gini = float('inf')
    
    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_y, right_y = y[X[:, feature] < threshold], y[X[:, feature] >= threshold]
            gini = len(left_y) * gini_impurity(left_y) + len(right_y) * gini_impurity(right_y)
            if gini < best_gini:
                best_gini = gini
                best_feature = feature
                best_threshold = threshold
    
    return best_feature, best_threshold

def build_tree(X, y):
    if len(np.unique(y)) == 1:
        return DecisionTreeNode(label=y[0])
    
    feature, threshold = best_split(X, y)
    left_X, left_y, right_X, right_y = split_data(X, y, feature, threshold)
    
    left_node = build_tree(left_X, left_y)
    right_node = build_tree(right_X, right_y)
    
    return DecisionTreeNode(feature=feature, threshold=threshold, left=left_node, right=right_node)

def predict(node, x):
    if node.label is not None:
        return node.label
    elif x[node.feature] < node.threshold:
        return predict(node.left, x)
    else:
        return predict(node.right, x)

if __name__ == '__main__':
    import numpy as np
    
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
                   [11, 12], [13, 14], [15, 16], [17, 18], [19, 20],
                   [21, 22], [23, 24], [25, 26], [27, 28], [29, 30],
                   [31, 32], [33, 34], [35, 36], [37, 38], [39, 40]])
    y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
    tree = build_tree(X, y)
    print(predict(tree, np.array([25, 30])))