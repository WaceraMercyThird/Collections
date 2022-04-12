# Collections


from collections import Counter

a = "aaaaabbbccc"

my_counter = Counter(a)
print(my_counter)

print(list(my_counter.elements()))

print(my_counter.most_common(1)[0][0])
