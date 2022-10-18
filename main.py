from wordcloud import WordCloud
import matplotlib.pyplot as plt

def st_ui(clean_text):
  wordcloud = WordCloud(width = 800, height =600,background_color ='white',min_font_size = 5,max_words=500).generate(clean_text)
  # plot the WordCloud image
  plt.figure(figsize = (15,10), facecolor = None)
  plt.imshow(wordcloud,interpolation="bilinear")
  plt.axis("off")
  plt.tight_layout(pad = 0)
  plt.show()
#   return image
