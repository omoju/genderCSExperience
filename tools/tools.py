import numpy as np
import pandas as pd
import pickle 
import scipy.stats as stats


dataPath = '/Users/omojumiller/Dropbox/Research/DissertationSubmission/'


CS10SPRING_DATA_1 = pd.read_csv(dataPath+'Data/CS10_Pre_Responses_Spring2015.csv')
CS10SPRING_DATA_2 = pd.read_csv(dataPath+'Data/CS10_Post_Responses_Spring2015.csv')
CS61A_DATA = pd.read_csv(dataPath+'Data/CS61A_Responses_Fall2014.csv')
MODEL_PICKLE_FILENAME = 'genderedCSExperience.pickle.dat'

## Column names
CS10SPRING_DATA_1.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1', 'name_2']

CS10SPRING_DATA_2.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1',
                            'snap_python','hiphop_d1','hiphop_d2','song_ct']

CS61A_DATA.columns = ['timestamp','consent','gender',
'reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1','atcs_3','atcs_4',
'atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3','atct_1',
'atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1','cltrcmp_2','classmtr',
'prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','priorcs10','name']



dd = pd.read_csv(dataPath+'Data/Data_Describe.csv')
dd.columns = ['dataDecription', 'dataKeys']
dataDescription = {}

for i, row in dd.iterrows():
    dataDescription[dd.dataKeys[i]] = dd.dataDecription[i]

def dataLookUp(item):
    try:
        print dataDescription[item]
    except:
        print item, "is not a valid data code"
            

def dataDescr():

    print "UC Berkeley Intro CS Student dataset"

    print "\nNotes"
    print "------"
    print "Data Set Characteristics:"

    print "\nNumber of Instances:{}".format(882)

    print "\nAttribute Information (in order):"

    print "\nSelf reported attitudes about CS"
    print "- atcs_1 I like to use computer science to solve problems."
    print "- atcs_2 I can learn to understand computing concepts."
    print "- atcs_3 I can achieve good grades (C or better) in computing courses."
    print "- atcs_4 I do not like using computer science to solve problems."
    print "- atcs_5 I am confident that I can solve problems by using computation."
    print "- atcs_6 The challenge of solving problems using computer science appeals to me."
    print "- atcs_7 I am comfortable with learning computing concepts."
    print "- atcs_8 I am confident about my abilities with regards to computer science."
    print "- atcs_9 I do think I can learn to understand computing concepts."

    print "\nGendered belief about CS ability"
    print "- atcsgender_1 Women are less capable of success in CS than men."
    print "- atcsgender_2 Women are smarter than men."
    print "- atcsgender_3 Men have better math and science abilities than women."

    print "\nCareer driven beliefs about CS"
    print "- atcsjob_1 Knowledge of computing will allow me to secure a good job."
    print "- atcsjob_2 My career goals do not require that I learn computing skills."

    print "\nSelf reported attitudes about computational thinking"
    print "- atct_1 I am good at solving a problem by thinking about similar problems I have solved before."
    print "- atct_2 I have good research skills."
    print "- atct_3 I am good at using online search tools."
    print "- atct_4 I am persistent at solving puzzles or logic problems."
    print "- atct_5 I know how to write computer programs."
    print "- atct_6 I am good at building things."
    print "- atct_7 I am good at ignoring irrelevant details to solve a problem."
    print "- atct_8 I know how to write a computer program to solve a problem."

    print "\nSelf reported attitudes about CS class belonging"
    print "- blg_1 In this class, I feel I belong."
    print "- blg_2 In this class, I feel awkward and out of place."
    print "- blg_3 In this class, I feel like my ideas count."
    print "- blg_4 In this class, I feel like I matter."

    print "\nSelf reported beliefs about collegiality"
    print "- clet_1 I work well in teams."
    print "- clet_2 I think about the ethical, legal, and social implications of computing."
    print "- cltrcmp_1 I am comfortable interacting with peers from different backgrounds than my own (based on race, sexuality, income, and so on.)"
    print "- cltrcmp_2 I have good cultural competence, or the ability to interact effectively with people from diverse backgrounds."

    print "\nDemographics"
    print "- gender Could I please know your gender"

    print "\nCS mentors and role models"
    print "- mtr_1 Before I came to UC Berkeley, I knew people who have careers in Computer Science."
    print "- mtr_2 There are people with careers in Computer Science who look like me."
    print "- mtr_3 I have role models within the Computer Science field that look like me."

    print "\nPrior collegiate CS exposure"
    print "- prcs_1 Did you take a CS course in High School?"
    print "- prcs_2 Did you have any exposure to Computer Science before UC Berkeley?"
    print "- prcs_3 Did a family member introduce you to Computer Science?"
    print "- prcs_4 Did you have a close family member who is a Computer Scientist or is affiliated with computing industry?"
    print "- prcs_5 Did your high school offer AP CS?"

    print "\nMissing Attribute Values: None"

    print "\nCreator: Omoju Miller"




def process( CS61A_DATA, CS10SPRING_DATA_1, CS10SPRING_DATA_2  ):


    ## Lets go ahead and filter out missing data.
    ## If the consent value is "I disagree", then drop that row from the data set.

    CS61A_DATA = CS61A_DATA[CS61A_DATA.consent == 'I agree']
    CS10SPRING_DATA_1 = CS10SPRING_DATA_1[CS10SPRING_DATA_1.consent == 'I agree']
    CS10SPRING_DATA_2 = CS10SPRING_DATA_2[CS10SPRING_DATA_2.consent == 'I agree']

    ## Combine all the different data samples representing the two collections from CS10 and the one collection from 61a


    frames = [CS10SPRING_DATA_1, CS10SPRING_DATA_2, CS61A_DATA]
    student_data = pd.concat(frames, keys=['pre', 'post','61a'])
    columnsNotNeeded = ['timestamp', 'consent','name', 'name_1', 'name_2',
                    'morecs','snap_python','hiphop_d1','hiphop_d2','song_ct', 'major']
    student_data.drop(columnsNotNeeded, axis=1, inplace=True)


    return student_data

def preprocess():
    return process( CS61A_DATA, CS10SPRING_DATA_1, CS10SPRING_DATA_2 )

def load_model():
    
    try:
        with open(MODEL_PICKLE_FILENAME, "r") as clf_infile:
            clf = pickle.load(clf_infile)
    except:
        print "Could not load model"
    return clf

def evaluate_chi(y, item):
    
    #contigency table of observed counts
    ct1 = pd.crosstab(y, item )

    #column percentages
    col_sum = ct1.sum(axis=0)
    col_percentage = ct1/col_sum 

    chi_squared_score, p_value, c, d = stats.chi2_contingency(ct1)
    print 'chi squared score: {:.2f} value: {:.12f}'.format(chi_squared_score, p_value)
    return chi_squared_score, p_value
