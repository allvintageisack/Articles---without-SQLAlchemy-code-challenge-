class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        topics = set()
        for article in self._articles:
            topics.add(article.magazine.category)
        return list(topics) if topics else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise Exception("Magazine name and category must be strings.")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters.")
        if len(category) == 0:
            raise Exception("Magazine category must have length greater than 0.")
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Magazine name must be a string.")
        self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("Magazine category must be a string.")
        self._category = new_category

    def add_article(self, article):
        self._articles.append(article)
        if article.author not in self._contributors:
            self._contributors.append(article.author)

    def articles(self):
        return self._articles

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors = [author for author in self._contributors if len(author.articles()) > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))


class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Article title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__._all.append(self)
        # Article._all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be an instance of Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        self._magazine = new_magazine
        

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise Exception("New title must be a string between 5 and 50 characters.")
        self._title = new_title

    @classmethod
    def all(cls):
        return cls._all[:]
    
   
