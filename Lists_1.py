sample = [2, 1, 3, 5, 4, 3, 8]
print(sample)
del sample[5]
print("Deleting the element at 5th index", sample)
sample.remove(4)
print("Deleting the element '4'", sample)
sample.sort()
print("Arranging the list ", sample)
sample.insert(3, 7)
print("Inserting the element '7' at 3rd index", sample)
sample.pop()
print("Deleting the last element", sample)
sample1 = [11, 15]
sample.extend(sample1)
print("Extending the elements of another elements in the current list, ", sample)
