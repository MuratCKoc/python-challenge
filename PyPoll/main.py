import csv
import os
import operator

# Filepath for input and output
write_txt = os.path.join("analysis","results.txt")

vote_csv = os.path.join("Resources","election_data.csv")

# Declare global variables
voteDict = {}
totalVotes = 0



# Sort the dictionary
def sortDict(e):
    return 

def byVoteCount(elem):
    return elem[1]

def printResults(l):
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    for iter in l:
        print(f"{iter[0]}: {iter[2]}% ({iter[1]})")
    print("-------------------------")
    print(f'Winner: {l[0][0]}')
    print("-------------------------")

def exportReport():
    with open(write_txt,"w") as fileX:
        
        fileX.write("Election Results\n")
        fileX.write("-------------------------\n")
        fileX.write(f"Total Votes: {totalVotes}\n")
        fileX.write("-------------------------\n")
        for iter in l:
            fileX.write(f"{iter[0]}: {iter[2]}% ({iter[1]})\n")
        fileX.write("-------------------------\n")
        fileX.write(f'Winner: {l[0][0]}\n')
        fileX.write("-------------------------")


# Percentage calculator function


# Main Loop
# Read file
with open(vote_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Increment the vote counter
        totalVotes += 1
        # Check if candidate exist
        if row[2] in voteDict :
            voteDict[row[2]] += 1
        # If not exist create a new record
        else:
            voteDict[row[2]] = 1

    # Sort the dictionary by voteCount 
    
    # Calculate Percentage 
    voteCandidates = voteDict.keys()
    voteCounts = voteDict.values()
    votePercentage = []
    for val in voteCounts:
        votePercentage.append(round((val/totalVotes)*100,3))

    # Zip list of values and sort them by number of votes
    l = list(zip(voteCandidates,voteCounts,votePercentage))
    l.sort(key=byVoteCount,reverse=True)

    # Print Results
    printResults(l)
    exportReport()
