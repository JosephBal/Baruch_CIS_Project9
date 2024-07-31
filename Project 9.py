# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:27:12 2023

@author: Admin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Program has a list variable named name_list that has a list of 500 common
# names (in all upper case)
# The sample program prints the count of names that have the letter 'H' and
# is greater than 6 characters long
###############################################################################

# the \ Python allows us to continue completing commands in subsequent line
list_of_names = \
['MARY', 'PATRICIA', 'LINDA', 'BARBARA', 'ELIZABETH', 'JENNIFER', 'MARIA',
'SUSAN', 'MARGARET', 'DOROTHY', 'LISA', 'NANCY', 'KAREN', 'BETTY', 'HELEN',
'SANDRA', 'DONNA', 'CAROL', 'RUTH', 'SHARON', 'MICHELLE', 'LAURA', 'SARAH',
'KIMBERLY', 'DEBORAH', 'JESSICA', 'SHIRLEY', 'CYNTHIA', 'ANGELA', 'MELISSA',
'BRENDA', 'AMY', 'ANNA', 'REBECCA', 'VIRGINIA', 'KATHLEEN', 'PAMELA',
'MARTHA', 'DEBRA', 'AMANDA', 'STEPHANIE', 'CAROLYN', 'CHRISTINE', 'MARIE',
'JANET', 'CATHERINE', 'FRANCES', 'ANN', 'JOYCE', 'DIANE', 'ALICE', 'JULIE',
'HEATHER', 'TERESA', 'DORIS', 'GLORIA', 'EVELYN', 'JEAN', 'CHERYL', 'MILDRED',
'KATHERINE', 'JOAN', 'ASHLEY', 'JUDITH', 'ROSE', 'JANICE', 'KELLY', 'NICOLE',
'JUDY', 'CHRISTINA', 'KATHY', 'THERESA', 'BEVERLY', 'DENISE', 'TAMMY',
'IRENE', 'JANE', 'LORI', 'RACHEL', 'MARILYN', 'ANDREA', 'KATHRYN', 'LOUISE',
'SARA', 'ANNE', 'JACQUELINE', 'WANDA', 'BONNIE', 'JULIA', 'RUBY', 'LOIS',
'TINA', 'PHYLLIS', 'NORMA', 'PAULA', 'DIANA', 'ANNIE', 'LILLIAN', 'EMILY',
'ROBIN', 'PEGGY', 'CRYSTAL', 'GLADYS', 'RITA', 'DAWN', 'CONNIE', 'FLORENCE',
'TRACY', 'EDNA', 'TIFFANY', 'CARMEN', 'ROSA', 'CINDY', 'GRACE', 'WENDY',
'VICTORIA', 'EDITH', 'KIM', 'SHERRY', 'SYLVIA', 'JOSEPHINE', 'THELMA',
'SHANNON', 'SHEILA', 'ETHEL', 'ELLEN', 'ELAINE', 'MARJORIE', 'CARRIE',
'CHARLOTTE', 'MONICA', 'ESTHER', 'PAULINE', 'EMMA', 'JUANITA', 'ANITA',
'RHONDA', 'HAZEL', 'AMBER', 'EVA', 'DEBBIE', 'APRIL', 'LESLIE', 'CLARA',
'LUCILLE', 'JAMIE', 'JOANNE', 'ELEANOR', 'VALERIE', 'DANIELLE', 'MEGAN',
'ALICIA', 'SUZANNE', 'MICHELE', 'GAIL', 'BERTHA', 'DARLENE', 'VERONICA',
'JILL', 'ERIN', 'GERALDINE', 'LAUREN', 'CATHY', 'JOANN', 'LORRAINE', 'LYNN',
'SALLY', 'REGINA', 'ERICA', 'BEATRICE', 'DOLORES', 'BERNICE', 'AUDREY',
'YVONNE', 'ANNETTE', 'JUNE', 'SAMANTHA', 'MARION', 'DANA', 'STACY', 'ANA',
'RENEE', 'IDA', 'VIVIAN', 'ROBERTA', 'HOLLY', 'BRITTANY', 'MELANIE', 'LORETTA',
'YOLANDA', 'JEANETTE', 'LAURIE', 'KATIE', 'KRISTEN', 'VANESSA', 'ALMA',
'SUE', 'ELSIE', 'BETH', 'JEANNE', 'VICKI', 'CARLA', 'TARA', 'ROSEMARY',
'EILEEN', 'TERRI', 'GERTRUDE', 'LUCY', 'TONYA', 'ELLA', 'STACEY', 'WILMA',
'GINA', 'KRISTIN', 'JESSIE', 'NATALIE', 'AGNES', 'VERA', 'WILLIE', 'CHARLENE',
'BESSIE', 'DELORES', 'MELINDA', 'PEARL', 'ARLENE', 'MAUREEN', 'COLLEEN',
'ALLISON', 'TAMARA', 'JOY', 'GEORGIA', 'CONSTANCE', 'LILLIE', 'CLAUDIA',
'JACKIE', 'MARCIA', 'TANYA', 'NELLIE', 'MINNIE', 'MARLENE', 'HEIDI', 'GLENDA',
'LYDIA', 'VIOLA', 'COURTNEY', 'MARIAN', 'STELLA', 'CAROLINE', 'DORA',
'JO', 'VICKIE', 'MATTIE', 'TERRY', 'MAXINE', 'IRMA', 'MABEL', 'MARSHA',
'MYRTLE', 'LENA', 'CHRISTY', 'DEANNA', 'PATSY', 'HILDA', 'GWENDOLYN',
'JENNIE', 'NORA', 'MARGIE', 'NINA', 'CASSANDRA', 'LEAH', 'PENNY', 'KAY',
'PRISCILLA', 'NAOMI', 'CAROLE', 'BRANDY', 'OLGA', 'BILLIE', 'DIANNE',
'TRACEY', 'LEONA', 'JENNY', 'FELICIA', 'SONIA', 'MIRIAM', 'VELMA', 'BECKY',
'BOBBIE', 'VIOLET', 'KRISTINA', 'TONI', 'MISTY', 'MAE', 'SHELLY', 'DAISY',
'RAMONA', 'SHERRI', 'ERIKA', 'KATRINA', 'CLAIRE', 'LINDSEY', 'LINDSAY',
'GENEVA', 'GUADALUPE', 'BELINDA', 'MARGARITA', 'SHERYL', 'CORA', 'FAYE',
'ADA', 'NATASHA', 'SABRINA', 'ISABEL', 'MARGUERITE', 'HATTIE', 'HARRIET',
'MOLLY', 'CECILIA', 'KRISTI', 'BRANDI', 'BLANCHE', 'SANDY', 'ROSIE', 'JOANNA',
'IRIS', 'EUNICE', 'ANGIE', 'INEZ', 'LYNDA', 'MADELINE', 'AMELIA', 'ALBERTA',
'GENEVIEVE', 'MONIQUE', 'JODI', 'JANIE', 'MAGGIE', 'KAYLA', 'SONYA', 'JAN',
'LEE', 'KRISTINE', 'CANDACE', 'FANNIE', 'MARYANN', 'OPAL', 'ALISON', 'YVETTE',
'MELODY', 'LUZ', 'SUSIE', 'OLIVIA', 'FLORA', 'SHELLEY', 'KRISTY', 'MAMIE',
'LULA', 'LOLA', 'VERNA', 'BEULAH', 'ANTOINETTE', 'CANDICE', 'JUANA', 'JEANNETTE',
'PAM', 'KELLI', 'HANNAH', 'WHITNEY', 'BRIDGET', 'KARLA', 'CELIA', 'LATOYA',
'PATTY', 'SHELIA', 'GAYLE', 'DELLA', 'VICKY', 'LYNNE', 'SHERI', 'MARIANNE',
'KARA', 'JACQUELYN', 'ERMA', 'BLANCA', 'MYRA', 'LETICIA', 'PAT', 'KRISTA',
'ROXANNE', 'ANGELICA', 'JOHNNIE', 'ROBYN', 'FRANCIS', 'ADRIENNE', 'ROSALIE',
'ALEXANDRA', 'BROOKE', 'BETHANY', 'SADIE', 'BERNADETTE', 'TRACI', 'JODY',
'KENDRA', 'JASMINE', 'NICHOLE', 'RACHAEL', 'CHELSEA', 'MABLE', 'ERNESTINE',
'MURIEL', 'MARCELLA', 'ELENA', 'KRYSTAL', 'ANGELINA', 'NADINE', 'KARI',
'ESTELLE', 'DIANNA', 'PAULETTE', 'LORA', 'MONA', 'DOREEN', 'ROSEMARIE',
'ANGEL', 'DESIREE', 'ANTONIA', 'HOPE', 'GINGER', 'JANIS', 'BETSY', 'CHRISTIE',
'FREDA', 'MERCEDES', 'MEREDITH', 'LYNETTE', 'TERI', 'CRISTINA', 'EULA',
'LEIGH', 'MEGHAN', 'SOPHIA', 'ELOISE', 'ROCHELLE', 'GRETCHEN', 'CECELIA',
'RAQUEL', 'HENRIETTA', 'ALYSSA', 'JANA', 'KELLEY', 'GWEN', 'KERRY', 'JENNA',
'TRICIA', 'LAVERNE', 'OLIVE', 'ALEXIS', 'TASHA', 'SILVIA', 'ELVIRA', 'CASEY',
'DELIA', 'SOPHIE', 'KATE', 'PATTI', 'LORENA', 'KELLIE', 'SONJA', 'LILA',
'LANA', 'DARLA', 'MAY', 'MINDY', 'ESSIE', 'MANDY', 'LORENE', 'ELSA', 'JOSEFINA',
'JEANNIE', 'MIRANDA', 'DIXIE', 'LUCIA', 'MARTA', 'FAITH', 'LELA', 'JOHANNA',
'SHARI', 'CAMILLE', 'TAMI', 'SHAWNA', 'ELISA', 'EBONY', 'MELBA', 'ORA',
'NETTIE', 'TABITHA', 'OLLIE', 'JAIME', 'WINIFRED', 'KRISTIE']

###############################################################################
# main program
# The program below returns a count of names that:
# (a) has the letter 'H' in them 
# and (b) has a length greater than 6
# uniue word: oranges
###############################################################################

A = 0
for name in list_of_names:
    if 'O' in name:
        A += 1
    elif 'R' in name:
        A += 1
    elif 'A' in name:
        A += 1
    elif 'N' in name:
        A += 1
    elif 'G' in name:
        A += 1
    elif 'E' in name:
        A += 1
    elif 'S' in name:
        A += 1

B = 0
for name in list_of_names:
    if name[-1] == 'O':
        B += 1
    elif name[-1] =='R':
        B += 1
    elif name[-1] =='A':
        B += 1
    elif name[-1] =='N':
        B += 1
    elif name[-1] =='G':
        B += 1
    elif name[-1] =='E':
        B += 1
    elif name[-1] =='S':
        B += 1
        
# print this count
print(A + B)


