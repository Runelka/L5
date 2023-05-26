array = [92, 32, 43, 55, 97, 34, 12, 33, 54]
index_min = array.index(min(array))
print (f"Соседние элементы от минимума: {array[index_min-1]} и {array[index_min+1]}")