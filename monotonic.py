def monotonic(list):

    k = all(list[i] < list[i+1] for i in range(len(list)-1))
    if k == False:
        k = all(list[i] > list[i + 1] for i in range(len(list) - 1))

    return print(k)
