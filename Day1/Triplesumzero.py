#triplet sum is equal to zero


sum = 0

def tripletsumzeroo(triplet_table):
    try:
        for i in range(len(triplet_table)):            
            for j in range(i+1,len(triplet_table)):
                all_sum  = triplet_table[i]+triplet_table[i+1]+triplet_table[j]
                if all_sum == sum:
                    print("tripletsumzero: {}  {}  {}".format(triplet_table[i],triplet_table[i+1],triplet_table[j]))
                else:
                    pass
    except IndexError:
        pass




triplet_table =  [0,-1,2,-3,1]
tripletsumzeroo(triplet_table = triplet_table)







