import random
import math

def LoadFromFile(newfile):
        answer = []
        f = open(newfile, "r")
        g = f.read()
        for line in g:
                answer.append(line)
        while(" " in answer):
                answer.remove(" ")
        while("\n" in answer):
                answer.remove("\n")
        x = len(answer)
        z = int(answer[0])
        answer.remove(answer[0])
        if z == int(math.sqrt(x-1)):
                return answer
        else:
                return "none"

def ComputeNeighbors(state):
        allsolutions = []
        case1 = []
        case2 = []
        case3 = []
        case4 = []
        p=0
        while p < len(state):
                case1.append((state[p]))
                case2.append((state[p]))
                case3.append((state[p]))
                case4.append((state[p]))
                p = p + 1
        z = findstar(case1)
        solution1 = []
        #moving to the left
        if z-1 > -1:
                solution1 = swap(case1, z, z-1)
                allsolutions.append(solution1)
        solution2 = []
        s = findstar(case2)
        #moving to the right
        if s+1 < 9:
                solution2 = swap(case2, s, s+1)
                allsolutions.append(solution2)
        solution3 = []
        #moving up
        u = findstar(case3)
        if u-3 > -1:
                solution3 = swap(case3, u, u-3)
                #print('solutions3 inside the if is ', solution3)
                allsolutions.append(solution3)
        solution4 = []
        #moving down
        t = findstar(case4)
        if t+3 < 9:
                solution4 = swap(case4, t, t+3)
                #print('solutions4 inside the if is ', solution4)
                allsolutions.append(solution4)
        #print('allsolutions is ', allsolutions)
        return allsolutions
        
def IsGoal(state):
        x = len(state)
        goal = []
        for i in range(1, x):
                goal.append(str(i))
        goal.append('*')
        newstate = []
        y=0
        return state == goal

def swap(state1, x1, x2):
        state1[x1], state1[x2] = state1[x2], state1[x1]
        return state1

def findstar(list):
        x=0
        while list[x] != "*":
                x = x + 1
        return x

def findswaps(list1, list2):
        x = 0
        y=""
        z=""
        while x<len(list1):
                if list1[x]==list2[x]:
                        x = x + 1
                else:
                        y = list1[x]
                        z = list2[x]
                        return ("We swapped " + y + " and " + z + ". ")

def backtrack(parents, end_state):
        current = end_state
        states_in_reverse = [end_state]
        while current:
                current = parents[tuple(current)]
                states_in_reverse.append(current)
        newstate = [states_in_reverse]
        newstates = reversed(newstate[-1])
        laststates = list(newstates)
        return laststates


def BFS(state):
        frontier = [state]
        discovered = set(state)
        parents = {tuple(state): None}
        while len(frontier) != 0:
                current_state = frontier.pop(0)
                discovered.add(tuple(current_state))
                if IsGoal(current_state):
                        answer = backtrack(parents, current_state)
                        print(answer)
                        newanswer = ""
                        t = 1
                        while t < (len(answer)-1):
                                newanswer = newanswer + findswaps(answer[t], answer[t+1])
                                t=t+1
                        return newanswer
                x=0
                for neighbor in ComputeNeighbors(current_state):
                        x=x+1
                        if tuple(neighbor) not in discovered:
                                frontier.append(neighbor)
                                discovered.add(tuple(neighbor))
                                parents[tuple(neighbor)] = current_state

def DFS(state):
        frontier = [state]
        discovered = set(state)
        parents = {tuple(state): None}
        while len(frontier) != 0:
                current_state = frontier.pop(0)
                discovered.add(tuple(current_state))
                if IsGoal(current_state):
                       answer2 = backtrack(parents, current_state)
                       newanswer = ""
                       t = 1
                       while t < (len(answer2)-1):
                               newanswer = newanswer + findswaps(answer2[t], answer2[t+1])
                               t=t +1
                       return newanswer
                               
                x=0
                for neighbor in ComputeNeighbors(current_state):
                        x = x + 1 
                        if tuple(neighbor) not in discovered:
                                frontier.insert(0, neighbor)
                                discovered.add(tuple(neighbor))
                                parents[tuple(neighbor)] = current_state
                          

def BidirectionalSearch(state):
        frontier = [state]
        backtier1 = ['1', '2', '3', '4', '5', '6', '7', '8']
        backtier1.append("*")
        backtier = [(backtier1)]
        newstate = tuple(backtier1)
        discovered = set()
        discovered.add(tuple(state))
        parents = {tuple(state): None}
        otherparents = {newstate: None}
        newdiscovered = set()
        newdiscovered.add(newstate)
        answer1 = ""
        answer2 = ""
        while len(frontier) != 0:
                current_state = frontier.pop(0)
                other_state = backtier.pop(0)
                tempcurrentstate = tuple(current_state)
                discovered.add((tempcurrentstate))
                newdiscovered.add(tuple(other_state))
                newanswer = ""
                newanswer3 = ""
                for x in discovered:
                        for y in newdiscovered:
                                if x == y:
                                        #current1=parents[x]
                                        #current2=parents[y]
                                        x1 = list(x)
                                        y1 = list(y)
                                        answer1 = backtrack(parents, x1)
                                        answer2 = backtrack(otherparents, y1)
                if len(answer1) > 0:
                        t=1
                        h=1
                        while t < (len(answer2)-1):
                                newanswer = newanswer + findswaps(answer2[t], answer2[t+1])
                                t = t + 1
                        while h < (len(answer1)-1):
                                newanswer3 = newanswer3 + findswaps(answer1[h], answer1[h+1])
                                h = h + 1
                        return newanswer3 + newanswer
                for neighbor in ComputeNeighbors(current_state):
                        if tuple(neighbor) not in discovered:
                                frontier.append(neighbor)
                                discovered.add(tuple(neighbor))
                                parents[tuple(neighbor)] = current_state
                for neighbor in ComputeNeighbors(other_state):
                        if tuple(neighbor) not in newdiscovered:
                                backtier.append(neighbor)
                                newdiscovered.add(tuple(neighbor))
                                otherparents[tuple(neighbor)] = other_state


def main():
        #nextdata = LoadFromFile("newtestfile.txt")
        #answer1 = BidirectionalSearch(nextdata)
        #answer1 = BFS(nextdata)
        #answer1 = DFS(nextdata)
        #print('the path we took is ',answer1)

                        


        
if __name__ == "__main__":
    main()
    
