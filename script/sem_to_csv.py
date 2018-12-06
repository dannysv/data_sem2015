from xml.dom import minidom
import csv
import sys
import os

def semeval_to_csv(path_xml_file, path_csv_file):
    xmldoc = minidom.parse(path_xml_file)

    review_tags = xmldoc.getElementsByTagName('Review')
    data = []

    for review_tag in review_tags:
        id_review = review_tag.getAttribute('rid')

        sentence_tags = review_tag.getElementsByTagName('sentence')
        for sentence_tag in sentence_tags:
            id_sentence = sentence_tag.getAttribute('id')

            text_tags = sentence_tag.getElementsByTagName('text')
            sentence_text=''
            for text_tag in text_tags:
                sentence_text = text_tag.firstChild.nodeValue.encode('utf-8')
                #sentence_text_replaced = sentence_text.replace('"','\'')
            opinion_tags = sentence_tag.getElementsByTagName('Opinion')
            for opinion_tag in opinion_tags:
                category = opinion_tag.getAttribute('category')
                polarity = opinion_tag.getAttribute('polarity')

                line = [id_review,id_sentence,sentence_text,category,polarity]
                data.append(line)

    with open(path_csv_file,'w') as csvfile:
        writer = csv.writer(csvfile, delimiter= '|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)
#path_xml_file_train = '../data/data_sem/ABSA-15_Laptops_Train_Data.xml'
#path_xml_file_test = '../data/data_sem/ABSA15_Laptops_Test.xml'

path_xml_file_train = '../data/data_sem/ABSA-15_Restaurants_Train_Final.xml'
path_xml_file_test = '../data/data_sem/ABSA15_Restaurants_Test.xml'

path_csv_file_train = '../data/data_csv/csv_train.csv'
path_csv_file_test = '../data/data_csv/csv_test.csv'
print('sem_to_csv...')
semeval_to_csv(path_xml_file_train,path_csv_file_train)
semeval_to_csv(path_xml_file_test,path_csv_file_test)
