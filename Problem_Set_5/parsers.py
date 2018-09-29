#Worked with Luke, Marissa, Harold
#############################################################
# PART #1
################################################################################
def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
#############################################################
# Test your part 1 code below.
    wordcount={}
    Trump_file = open(filename)
    for word in Trump_file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print(wordcount)
    Trump_file.close();
(countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Trump_2017.txt'))