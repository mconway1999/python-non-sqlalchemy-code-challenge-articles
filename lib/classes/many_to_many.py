class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
         if (not hasattr(self,'title')) and type(value) == str and 5 <= len(value) <= 50:
             self._title=value 

    @property 
    def author(self):
        return self._author 
    
    @author.setter 
    def author (self,value):
        if type (value) == Author:
            self._author = value  

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter 
    def magazine (self,value):
        if type (value) == Magazine:
            self._magazine = value  
        

class Author:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self,value):
        if (not hasattr(self,'name')) and type(value) == str and len(value) > 0:
            self._name = value

    def articles(self):
         return [article for article in Article.all if article.author is self]
    
    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author is self]))


    def add_article(self, magazine, title):
        return Article (self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        else:
            return [magazine.category for magazine in self.magazines()] 

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and 2 <= len(value) <= 16:
            self._name = value

    @property 
    def category(self):
        return self._category
    
    @category.setter
    def category (self,value):
        if type(value) == str and 0 < len(value):
            self._category = value 


    def articles(self):
         return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        else:
             return [article.title for article in self.articles()]

    def contributing_authors(self):
        contributing_authors_list = [author for author in self.contributors() if self.author_has_more_than_two(author)]
        if len(contributing_authors_list) == 0:
            return None 
        else: 
            return contributing_authors_list

    def author_has_more_than_two(self, author):
        if len([article for article in author.articles() if article.magazine is self]) > 2:
            return True
        else:
            return False