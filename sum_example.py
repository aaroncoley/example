# a function something that sums up from the begining to the end
def sum(num):
    result = 0
    for i in range(num):
        result = result + num - i
        print(result)

sum(5)
